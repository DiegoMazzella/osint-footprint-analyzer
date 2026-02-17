# Metodología OSINT

## 🎯 Objetivo
El propósito de esta metodología es guiar un análisis estructurado de la huella digital de una empresa ficticia, siguiendo principios éticos y buenas prácticas de ciberinteligencia.

---

## 1. Definición de requerimientos de inteligencia
- Identificar qué información es relevante y por qué.
- Definir objetivos claros: activos, exposición y riesgos.
- Limitar el análisis a lo estrictamente necesario.

---

## 2. Identificación de activos y superficie digital
- Dominios web y subdominios
- Direcciones de correo electrónico corporativas
- Presencia en redes sociales
- Documentos públicos y metadatos
- Posibles filtraciones en brechas conocidas

---

## 3. Recolección de información
- **Manual:** búsqueda en Google, LinkedIn, redes sociales, bases de datos públicas
- **Automatizada:** scripts en Python para analizar patrones de correos, subdominios y metadatos
- **Registro:** almacenar toda la información en la carpeta `data/raw` para trazabilidad

---

## 4. Validación y enriquecimiento
- Comprobar consistencia de datos recolectados
- Correlacionar información entre distintas fuentes
- Identificar falsos positivos o duplicados
- Guardar resultados procesados en `data/processed`

---

## 5. Análisis de riesgos y exposición
- Evaluar riesgos de ingeniería social, phishing y reputación
- Identificar activos expuestos innecesariamente
- Clasificar riesgos por impacto potencial

---

## 6. Elaboración de informes
- Crear **resumen ejecutivo** para perfiles no técnicos (`reports/resumen_ejecutivo.md`)
- Crear **informe técnico detallado** (`reports/informe_tecnico.md`)
- Adjuntar capturas, evidencia y hallazgos
- Recomendar mejoras o mitigaciones

---

## ⚖️ Principios fundamentales
- Legalidad y ética en todas las fases
- Transparencia metodológica
- Minimización de datos recolectados
- Documentación clara para auditoría y revisión
