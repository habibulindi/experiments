#!/bin/bash
set -e

echo "🚀 Запуск стека мониторинга..."
cd "$(dirname "$0")"
docker-compose up -d

echo "✅ Сервисы запущены:"
echo "   • Grafana: http://localhost:3000 (admin/admin123)"
echo "   • Prometheus: http://localhost:9090"
echo "   • Alertmanager: http://localhost:9093"
echo "   • Loki: http://localhost:3100"
echo ""
echo "📊 Не забудьте:"
echo "   1. Проверить Targets в Prometheus"
echo "   2. Импортировать дашборд в Grafana"
echo "   3. Настроить SMTP в alertmanager.yml"
