# SLI/SLO для API

## SLI 1: Доступность (Availability)
- **Формула:** `(Успешные запросы / Все запросы) × 100%`
- **SLO:** 99.9% за 30 дней
- **Метрика:** `http_requests_total{status=~"2..|3.."}`

## SLI 2: Задержка (Latency)
- **Формула:** 95-й перцентиль времени ответа
- **SLO:** < 500 мс за 5 минут
- **Метрика:** `histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))`

## SLI 3: Частота ошибок (Error Rate)
- **Формула:** `(5xx / Все запросы) × 100%`
- **SLO:** < 1% за 5 минут
- **Метрика:** `sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) × 100`
