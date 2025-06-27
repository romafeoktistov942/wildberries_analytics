from django.core.management.base import BaseCommand
from analytics.parser import parse_products
import sys


class Command(BaseCommand):
    help = "Парсит товары с Wildberries по запросу"

    def add_arguments(self, parser):
        parser.add_argument(
            "query", type=str, help='Поисковой запрос, например: "ноутбук"'
        )

    def handle(self, *args, **options):
        query = options["query"]
        self.stdout.write(f"Начинаем парсинг по запросу: {query}")
        try:
            parse_products(query)
            self.stdout.write(self.style.SUCCESS("Парсинг завершён успешно!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Ошибка при парсинге: {e}"))
            sys.exit(1)
