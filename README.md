# Coimbatore Chaat

A Coimbatore-first street-food and chaat marketplace with its own delivery-partner network.

## Product scope
- Street food and chaat only.
- Launch area: Coimbatore city.
- Customer ordering through web, Android and iOS.
- Restaurant partners and delivery partners are onboarded only after admin approval.
- One shared API and database for all clients.
- Own delivery operations; no third-party delivery aggregator dependency.

## Repository layout
- `apps/web` — customer website (Netlify).
- `apps/mobile` — planned Expo customer app.
- `apps/delivery` — planned delivery-partner app.
- `apps/partner-admin` — planned restaurant/admin portal.
- `services/api` — FastAPI backend.
- `docs` — product and implementation notes.

## Run the API locally
```bash
cd services/api
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
The API uses SQLite by default for local development. Set `DATABASE_URL` to a PostgreSQL connection string for shared environments.

## Run the website locally
```bash
cd apps/web
npm install
npm run dev
```
Set `VITE_API_BASE_URL` to the API base URL (for example, `http://localhost:8000`). The website does not silently substitute fake restaurants when the API is unavailable.

## Deployment
Netlify build settings are defined in `netlify.toml`. The FastAPI service and PostgreSQL database must be deployed separately; Netlify hosts the web frontend, not the persistent API/database.

## Current implementation status
- [x] Initial repository and backend foundation
- [x] Database-backed restaurant and menu read endpoints
- [x] Customer web browsing foundation
- [ ] Authentication and role-based access
- [ ] Restaurant onboarding and admin approval
- [ ] Cart, checkout, payments and order lifecycle
- [ ] Delivery-partner dispatch and live tracking
- [ ] Expo Android/iOS customer app
- [ ] Delivery-partner app
- [ ] Production deployment and end-to-end testing

Do not treat unchecked items as implemented.