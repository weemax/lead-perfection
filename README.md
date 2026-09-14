# lead-perfection
lead-perfection is a Python library that provides a simple interface for interaction with [LeadPerfection](https://app.swaggerhub.com/apis/LeadPerfection/Examples/1.0) methods, packaging them into an easy-to-use format. It abstracts authentication, request formatting, and endpoint access to make LeadPerfection integrations easier for developers building automations, backend services, and CRM tooling.

## Benefits & Features
- Simple authentication workflow
- Organized client and module structure (client, customers, leads, etc.)
- Reduces need to write boilerplate requests for LeadPerfection API calls

## Installation
```bash
pip install lead-perfection
```

## Configuration
Credentials are passed to `Client` as arguments - the library never reads them from disk.
Keep them out of source control by putting them in a `.env` file (already gitignored):

```bash
cp .env.example .env   # then fill in your values
```

```bash
# .env
LP_SERVER_ID=apitest   # 'apitest' for the sandbox, 'api' for production
LP_CLIENT_ID=
LP_USERNAME=
LP_PASSWORD=
LP_APP_KEY=
```

## Usage Example
See `example.py` for a runnable version that loads the `.env` file above.

```python
import os

import lead_perfection as lp

client = lp.client.Client(
    os.environ['LP_SERVER_ID'],
    os.environ['LP_CLIENT_ID'],
    os.environ['LP_USERNAME'],
    os.environ['LP_PASSWORD'],
    os.environ['LP_APP_KEY'],
)

# Authenticate and retrieve an access token
access_token = client.authenticate()['access_token']

# Access the Menu endpoint using the obtained token
lp_menu = lp.menu.Menu(server_id=client.server_id, access_token=access_token)
print("Menu Result:", lp_menu.get_menu())

# Access the Leads endpoint using the obtained token
lp_leads = lp.leads.Leads(server_id=client.server_id, access_token=access_token)
print("Leads Confirmed Message Result:", lp_leads.get_leads_confirmed_message())
```

Endpoint access is granted per account. A valid token can still return
`403 User does not have permission to execute action '<Action>'` for endpoints
your LeadPerfection account is not entitled to.

## Project Structure
 - `canvass.py` - Wrapper for all canvass-related API calls
 - `client.py` - Handles authentication with the LeadPerfection API
 - `custom.py` - Wrapper for custom API calls
 - `customers.py` - Wrapper for all customer-related API calls
 - `downloads.py` - Wrapper for all download-related API calls
 - `file.py` - Wrapper for all file-related API calls
 - `installer.py` - Wrapper for all installer-related API calls
 - `leads.py` - Wrapper for all lead-related API calls
 - `menu.py` - Wrapper for all menu-related API calls
 - `sales.py` - Wrapper for all sales-related API calls
 - `utils.py` - Abstraction for http requests and header setup

## Extending the Library
`lead-perfection` is structured so you can easily add new endpoint wrappers:
 - Create a new module file (e.g., `appointments.py`)
 - Implement functions that call the appropriate LeadPerfection API paths

## Local Development
```bash
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/python example.py
```

## Requirements
- Python 3.8+

## License
This project is licensed under the MIT License.

## Links
- Source Code: https://github.com/weemax/lead-perfection
- Issues: https://github.com/weemax/lead-perfection/issues
