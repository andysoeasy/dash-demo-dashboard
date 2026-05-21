from pathlib import Path

MONTH = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
YEARS = [2025, 2026]
WEEKS = list(range(1, 6))
QUARTERS = ['I', 'II', 'III', 'IV']

COMPANIES = [
    'EURGBP=X',
    'AAPL', 
    'MSFT', 
    'GOOGL', 
    'AMZN', 
    'META', 
    'TSLA', 
    'NVDA',
    'TSM',
    'BTC-USD',
    'ETH-USD'
]


STRATEGIES = ['MR']
CATEGORIES = {
    company: category 
    for company, category in zip(COMPANIES, [f'category-{i}' for i in range(1, len(COMPANIES) + 1)])
}
DATA_DIR = Path('data')

COLOR_MAP = {
    'AAPL': '#1f77b4',
    'MSFT': '#ff7f0e',
    'GOOGL': '#2ca02c',
    'AMZN': '#d62728',
    'META': '#9467bd',
    'TSLA': '#8c564b',
    'NVDA': '#e377c2',
    'NFLX': '#7f7f7f',
}

COLORS_BASE_THEME = {
    'base_font': '#262626',
    'background_chart': '#f8f9fa',
    'background_color': '#ADC2FF',
    'main_title': '#3366FF',
    'chart_title': '#DA3248',
    'base_color': '#CCCCCC',
    'categories': {
        'category-1': '#3366FF',
        'category-2': '#C2C61C',
        'category-3': '#DA7A32',
        'category-4': '#C04052',
        'category-5': "#40C07C",
        'category-6': "#A040C0",
        'category-7': "#388CD1",
        'category-8': "#e377c2",
        'category-9': "#8c564b",
        'category-10': "#9467bd",
        'category-11': "#7f7f7f",
        'category-12': "#1f77b4"
    }
}