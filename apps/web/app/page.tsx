import { InventoryPanel } from "./InventoryPanel";

const capabilities = [
  "Inventario trazable",
  "Predicciones reproducibles",
  "Alertas priorizadas",
];

export default function Home() {
  return (
    <main className="shell">
      <p className="eyebrow">DeepPharma · tracer bullet</p>
      <h1>Gestión inteligente de medicamentos esenciales.</h1>
      <p className="lede">
        Primer vertical ejecutable: una interfaz mínima para validar el límite
        entre inventario, predicciones y alertas.
      </p>
      <section aria-label="Capacidades iniciales" className="capabilities">
        {capabilities.map((capability) => (
          <article key={capability}>{capability}</article>
        ))}
      </section>
      <p className="status">API y persistencia: en construcción.</p>
      <section aria-labelledby="inventory-title" className="inventory">
        <h2 id="inventory-title">Inventario actual</h2>
        <InventoryPanel />
      </section>
    </main>
  );
}
