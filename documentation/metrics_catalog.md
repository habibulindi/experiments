# Каталог метрик

## Приложение
| Метрика | Тип | Описание | Лейблы |
|---------|-----|----------|--------|
| `http_requests_total` | Counter | Всего HTTP запросов | method, endpoint, status |
| `http_request_duration_seconds` | Histogram | Время ответа | endpoint |
| `active_requests` | Gauge | Активные запросы | - |
| `users_processed_total` | Counter | Обработано пользователей | source |

## Инфраструктура (Node Exporter)
| Метрика | Тип | Описание |
|---------|-----|----------|
| `node_cpu_seconds_total` | Counter | Время CPU по режимам |
| `node_memory_MemAvailable_bytes` | Gauge | Доступная память |
| `node_filesystem_avail_bytes` | Gauge | Свободное место на диске |
