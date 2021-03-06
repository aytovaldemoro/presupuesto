import project.settings as settings
from django.conf import settings

def analytics_processor(request):
    return { 'analytics_code': '' if not hasattr(settings, 'ANALYTICS_CODE') else settings.ANALYTICS_CODE }

def cookies_url_processor(request):
    return { 'cookies_url': False if not hasattr(settings, 'COOKIES_URL') else settings.COOKIES_URL }

def show_options_processor(request):
    return {
      'show_payments':            hasattr(settings, 'SHOW_PAYMENTS') and settings.SHOW_PAYMENTS,
      'show_tax_receipt':         hasattr(settings, 'SHOW_TAX_RECEIPT') and settings.SHOW_TAX_RECEIPT,
      'show_counties_and_towns':  hasattr(settings, 'SHOW_COUNTIES_AND_TOWNS') and settings.SHOW_COUNTIES_AND_TOWNS
    }

def main_entity_processor(request):
    return {
      'main_entity_web_url':       hasattr(settings, 'MAIN_ENTITY_WEB_URL') and settings.MAIN_ENTITY_WEB_URL,
      'main_entity_legal_url':     hasattr(settings, 'MAIN_ENTITY_LEGAL_URL') and settings.MAIN_ENTITY_LEGAL_URL,
      'main_entity_privacy_url':   hasattr(settings, 'MAIN_ENTITY_PRIVACY_URL') and settings.MAIN_ENTITY_PRIVACY_URL
    }

def data_sources_processor(request):
    return {
      'data_source_budget':        hasattr(settings, 'DATA_SOURCE_BUDGET') and settings.DATA_SOURCE_BUDGET,
      'data_source_population':    hasattr(settings, 'DATA_SOURCE_POPULATION') and settings.DATA_SOURCE_POPULATION,
      'data_source_inflation':     hasattr(settings, 'DATA_SOURCE_INFLATION') and settings.DATA_SOURCE_INFLATION
    }

def search_entities_processor(request):
    return { 'search_entities': False if not hasattr(settings, 'SEARCH_ENTITIES') else settings.SEARCH_ENTITIES }

def debug(context):
    return { 'debug': settings.DEBUG }
