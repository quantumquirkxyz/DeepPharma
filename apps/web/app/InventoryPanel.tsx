"use client";

import { useCallback, useEffect, useState } from "react";

type InventoryItem = {
  id: number;
  medicamento_id: number;
  centro_salud_id: number;
  stock_actual: number;
  actualizado_en: string;
};

type CatalogItem = { id: number; nombre: string };
type AlertItem = {
  id: number;
  inventario_id: number;
  nivel: string;
  estado: string;
};

const apiUrl = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export function InventoryPanel() {
  const [token, setToken] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [authMessage, setAuthMessage] = useState("");
  const [items, setItems] = useState<InventoryItem[]>([]);
  const [medicamentos, setMedicamentos] = useState<CatalogItem[]>([]);
  const [centros, setCentros] = useState<CatalogItem[]>([]);
  const [alerts, setAlerts] = useState<AlertItem[]>([]);
  const [state, setState] = useState<"loading" | "ready" | "error">("loading");
  const [medicamentoId, setMedicamentoId] = useState("");
  const [centroSaludId, setCentroSaludId] = useState("");
  const [stockActual, setStockActual] = useState("");
  const [formMessage, setFormMessage] = useState("");

  const loadInventory = useCallback(() => {
    if (!token) return;
    fetch(`${apiUrl}/api/v1/inventory`, {
      headers: { Authorization: `Bearer ${token}` },
    })
      .then((response) => {
        if (!response.ok) throw new Error("No se pudo consultar inventario");
        return response.json() as Promise<InventoryItem[]>;
      })
      .then((data) => {
        setItems(data);
        setState("ready");
      })
      .catch(() => setState("error"));
  }, [token]);

  useEffect(() => {
    loadInventory();
    if (!token) return;
    Promise.all([
      fetch(`${apiUrl}/api/v1/catalog/medicamentos`).then((response) => response.json()),
      fetch(`${apiUrl}/api/v1/catalog/centros-salud`).then((response) => response.json()),
      fetch(`${apiUrl}/api/v1/alerts`, {
        headers: { Authorization: `Bearer ${token}` },
      }).then((response) => response.json()),
    ])
      .then(
        ([medicineData, centerData, alertData]: [
          CatalogItem[],
          CatalogItem[],
          AlertItem[],
        ]) => {
        setMedicamentos(medicineData);
        setCentros(centerData);
        setAlerts(alertData);
        setMedicamentoId(String(medicineData[0]?.id ?? ""));
        setCentroSaludId(String(centerData[0]?.id ?? ""));
        },
      )
      .catch(() => setState("error"));
  }, [loadInventory, token]);

  async function login(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const body = new URLSearchParams({ username, password });
    const response = await fetch(`${apiUrl}/token`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body,
    });
    if (!response.ok) {
      setAuthMessage("Credenciales inválidas.");
      return;
    }
    const data = (await response.json()) as { access_token: string };
    setToken(data.access_token);
    setAuthMessage("");
    setState("loading");
  }

  async function submitUpdate(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setFormMessage("");

    const response = await fetch(`${apiUrl}/api/v1/inventory`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        medicamento_id: Number(medicamentoId),
        centro_salud_id: Number(centroSaludId),
        stock_actual: Number(stockActual),
      }),
    });

    if (!response.ok) {
      setFormMessage("No se pudo registrar la actualización.");
      return;
    }

    setStockActual("");
    setFormMessage("Actualización registrada.");
    await fetch(`${apiUrl}/api/v1/risk/evaluate`, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}` },
    });
    const alertsResponse = await fetch(`${apiUrl}/api/v1/alerts`, {
      headers: { Authorization: `Bearer ${token}` },
    });
    if (alertsResponse.ok) {
      setAlerts((await alertsResponse.json()) as AlertItem[]);
    }
    loadInventory();
  }

  async function acknowledgeAlert(alertId: number) {
    const response = await fetch(`${apiUrl}/api/v1/alerts/${alertId}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        estado: "RECONOCIDA",
        comentario: "Reconocida desde el dashboard",
      }),
    });
    if (response.ok) {
      setAlerts((current) =>
        current.map((alert) =>
          alert.id === alertId ? { ...alert, estado: "RECONOCIDA" } : alert,
        ),
      );
    }
  }

  if (!token) {
    return (
      <form className="login-form" onSubmit={login}>
        <label>
          Usuario
          <input required value={username} onChange={(event) => setUsername(event.target.value)} />
        </label>
        <label>
          Contraseña
          <input
            required
            type="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        </label>
        <button type="submit">Iniciar sesión</button>
        {authMessage && <p role="alert">{authMessage}</p>}
      </form>
    );
  }
  if (state === "loading") return <p>Consultando inventario…</p>;
  if (state === "error") return <p role="alert">No se pudo cargar el inventario.</p>;
  return (
    <>
      <form className="inventory-form" onSubmit={submitUpdate}>
        <label>
          Medicamento
          <select
            required
            value={medicamentoId}
            onChange={(event) => setMedicamentoId(event.target.value)}
          >
            <option value="">Seleccionar medicamento</option>
            {medicamentos.map((item) => (
              <option key={item.id} value={item.id}>
                {item.nombre}
              </option>
            ))}
          </select>
        </label>
        <label>
          Centro de salud
          <select
            required
            value={centroSaludId}
            onChange={(event) => setCentroSaludId(event.target.value)}
          >
            <option value="">Seleccionar centro</option>
            {centros.map((item) => (
              <option key={item.id} value={item.id}>
                {item.nombre}
              </option>
            ))}
          </select>
        </label>
        <label>
          Stock actual
          <input
            min="0"
            required
            type="number"
            value={stockActual}
            onChange={(event) => setStockActual(event.target.value)}
          />
        </label>
        <button type="submit">Registrar actualización</button>
      </form>
      {formMessage && <p role="status">{formMessage}</p>}
      {alerts.length > 0 && (
        <aside className="alert-panel" aria-labelledby="alerts-title">
          <h3 id="alerts-title">Alertas activas</h3>
          <ul className="inventory-list">
            {alerts.map((alert) => (
              <li key={alert.id}>
                <strong>{alert.nivel}</strong> · Inventario {alert.inventario_id} ·{" "}
                {alert.estado}
                {alert.estado === "NUEVA" && (
                  <button
                    className="alert-action"
                    type="button"
                    onClick={() => acknowledgeAlert(alert.id)}
                  >
                    Reconocer
                  </button>
                )}
              </li>
            ))}
          </ul>
        </aside>
      )}
      {items.length === 0 ? (
        <p>No hay inventario registrado todavía.</p>
      ) : (
        <ul className="inventory-list">
            {items.map((item) => (
              <li key={item.id}>
                Medicamento{" "}
                {medicamentos.find((medicine) => medicine.id === item.medicamento_id)
                  ?.nombre ?? item.medicamento_id}{" "}
                · Centro{" "}
                {centros.find((center) => center.id === item.centro_salud_id)?.nombre ??
                  item.centro_salud_id}{" "}
                · <strong>{item.stock_actual} unidades</strong>
              </li>
          ))}
        </ul>
      )}
    </>
  );
}
