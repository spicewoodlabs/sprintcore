from core.parser import parse_prd

def test_parse_prd_mock():
    prompt = "You are a product manager. Convert {{REQUIREMENTS}} to epics/stories."
    md = "# Login Page\nUsers should be able to login with email and password."
    result = parse_prd(md, prompt, model='gpt-3.5-turbo', mock=True)
    assert isinstance(result, list)
    assert 'epic_name' in result[0]
