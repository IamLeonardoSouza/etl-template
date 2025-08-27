from src.extract.api_extract import extract_api

# Teste simples para a função de extração da API
def test_extract_api():
    df = extract_api()
    assert df.shape[0] > 0
