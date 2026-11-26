# Triage and project labels

Triage is part of the standard project flow. Incoming issues are classified before implementation starts.

## Canonical role mappings

| Canonical role | Tracker label | Meaning |
| --- | --- | --- |
| `needs-triage` | `status:triage` | Maintainer needs to evaluate the item |
| `needs-info` | `status:needs-info` | Waiting for clarification or requirements |
| `ready-for-agent` | `status:ready` | Fully specified and ready for agent implementation |
| `ready-for-human` | `status:review` | Requires human implementation, review, or merge |
| `wontfix` | `status:out-of-scope` | Will not be actioned |

## Taxonomy

### Workflow

`status:triage`, `status:needs-info`, `status:blocked`, `status:ready`, `status:in-progress`, `status:review`, `status:done`, `status:out-of-scope`

El campo nativo `Status` del Project debe reflejar esta misma máquina; no se
define una fase independiente.

### Work type

`type:feature`, `type:bug`, `type:architecture`, `type:documentation`, `type:spec`, `type:sub-spec`, `type:research`, `type:maintenance`, `type:security`

`type:spec` identifica un Parent Spec y `type:sub-spec` identifica una
Sub-Spec. Ambos sustituyen `type:documentation` para evitar dos labels de tipo
en el mismo Issue. `type:documentation` permanece para documentación que no es
una especificación.

### Engineering discipline

`area:requirements`, `area:architecture`, `area:implementation`, `area:testing`, `area:quality`, `area:operations`, `area:observability`, `area:security`, `area:documentation`, `area:skills-platform`

### Priority

`priority:critical`, `priority:high`, `priority:medium`, `priority:low`

### Risk

`risk:critical`, `risk:high`, `risk:medium`, `risk:low`, `risk:unknown`

Priority and risk are independent dimensions. Use at most one label from each
family and explain the risk in the work-item body.

Use the most specific applicable labels. This file defines the repository vocabulary; remote GitHub labels must be created or reconciled separately with explicit tracker mutation approval.
