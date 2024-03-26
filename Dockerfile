FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install Flask requests selenium
EXPOSE 30000
ENV FLASK_ENV=production
CMD ["python", "main_score.py"] && ["python", "e2e.py"]