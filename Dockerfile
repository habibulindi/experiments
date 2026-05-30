# ============ Стадия сборки (build) ============
FROM python:3.11-slim AS builder

# Устанавливаем системные зависимости, необходимые для сборки wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем только файл с зависимостями и устанавливаем их
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# ============ Финальная стадия (production) ============
FROM python:3.11-slim

# Создаём непривилегированного пользователя (хорошая практика безопасности)
RUN useradd --create-home --shell /bin/bash appuser

WORKDIR /app

# Копируем установленные пакеты из builder-образа
COPY --from=builder /root/.local /home/appuser/.local

# Копируем исходный код приложения
COPY src/ src/

# Переключаемся на пользователя appuser
USER appuser

# Добавляем локальные пакеты в PATH
ENV PATH="/home/appuser/.local/bin:$PATH"

# Указываем порт (если веб-приложение)
EXPOSE 5000

# Команда запуска (замени на свою, если используется не Flask)
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
