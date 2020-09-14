import json
def test_hello(app):
  client = app.test_client()
  resp = client.get('/')
  data = data = json.loads(resp.data.decode())
  assert resp.status_code == 200
  assert 'App is running' in data['message']