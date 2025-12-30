# API Documentation

## Regenera360 Medical Ecosystem REST API

Base URL: `http://localhost:8000`

### Authentication

Currently, the API doesn't require authentication. For production, implement authentication using JWT tokens or API keys.

### Response Format

All responses are in JSON format.

Success response:
```json
{
  "status": "success",
  "data": {...}
}
```

Error response:
```json
{
  "status": "error",
  "detail": "Error message"
}
```

## Endpoints

### System Endpoints

#### GET /
Get API information

**Response:**
```json
{
  "message": "Regenera360 Medical Ecosystem API",
  "version": "1.0.0",
  "status": "active"
}
```

#### GET /health
Health check endpoint

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2025-12-30T16:59:35.991Z"
}
```

### AI Endpoints

#### POST /ai/query
Query AI for medical information

**Request Body:**
```json
{
  "query": "¿Cuáles son los síntomas de la diabetes?",
  "max_length": 200
}
```

**Response:**
```json
{
  "query": "¿Cuáles son los síntomas de la diabetes?",
  "response": "AI generated response..."
}
```

#### POST /ai/analyze
Analyze medical text

**Query Parameters:**
- `text` (string, required): Text to analyze

**Response:**
```json
{
  "text": "Original text",
  "sentiment": {...},
  "length": 100,
  "word_count": 20
}
```

### WhatsApp Endpoints

#### POST /whatsapp/send
Send WhatsApp message

**Request Body:**
```json
{
  "to": "whatsapp:+1234567890",
  "body": "Your message here",
  "media_url": "https://example.com/image.jpg" // optional
}
```

**Response:**
```json
{
  "message_sid": "SMxxxxxxxxx",
  "status": "sent"
}
```

#### POST /whatsapp/appointment-reminder
Send appointment reminder via WhatsApp

**Request Body:**
```json
{
  "to": "whatsapp:+1234567890",
  "patient_name": "Juan Pérez",
  "appointment_date": "2025-01-15",
  "appointment_time": "10:00 AM"
}
```

**Response:**
```json
{
  "message_sid": "SMxxxxxxxxx",
  "status": "sent"
}
```

### Wix Endpoints

#### GET /wix/site-info
Get Wix site information

**Response:**
```json
{
  "siteId": "...",
  "siteName": "...",
  ...
}
```

#### GET /wix/contacts
Get Wix contact submissions

**Response:**
```json
{
  "contacts": [...],
  "count": 10
}
```

### Meta Ads Endpoints

#### GET /meta/campaigns
Get Meta Ads campaigns

**Query Parameters:**
- `status` (string, optional): Filter by status

**Response:**
```json
{
  "campaigns": [...],
  "count": 5
}
```

#### GET /meta/insights
Get Meta Ads account insights

**Response:**
```json
{
  "impressions": 1000,
  "clicks": 50,
  "spend": 100.00,
  ...
}
```

### Google Business Endpoints

#### GET /google/location
Get Google Business location info

**Response:**
```json
{
  "name": "...",
  "address": "...",
  ...
}
```

#### GET /google/insights
Get Google Business insights

**Response:**
```json
{
  "location": "...",
  "metric_type": "ALL",
  ...
}
```

### GitHub Endpoints

#### GET /github/stats
Get GitHub repository statistics

**Response:**
```json
{
  "name": "Ecosistema-Regenera360Fenix",
  "stars": 0,
  "forks": 0,
  "open_issues": 0,
  ...
}
```

#### GET /github/issues
Get GitHub issues

**Query Parameters:**
- `state` (string, optional): Filter by state (open, closed, all)

**Response:**
```json
{
  "issues": [
    {
      "number": 1,
      "title": "Issue title"
    }
  ]
}
```

### Automation Endpoints

#### POST /automation/daily-tips
Trigger daily health tips sending

**Response:**
```json
{
  "status": "scheduled",
  "message": "Daily health tips will be sent"
}
```

#### POST /automation/daily-report
Generate daily report

**Response:**
```json
{
  "date": "2025-12-30",
  "github_stats": {...},
  "wix_contacts": 10,
  ...
}
```

#### POST /automation/patient-inquiry
Handle patient inquiry with AI

**Query Parameters:**
- `patient_id` (string, required): Patient identifier
- `inquiry` (string, required): Patient's inquiry

**Response:**
```json
{
  "patient_id": "...",
  "inquiry": "...",
  "response": "AI generated response",
  "message_sid": "...",
  "timestamp": "2025-12-30T16:59:35.991Z"
}
```

## Error Codes

- `400` Bad Request - Invalid parameters
- `404` Not Found - Resource not found
- `500` Internal Server Error - Server error

## Rate Limiting

Currently, no rate limiting is implemented. For production, implement rate limiting based on your requirements.

## Examples

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# AI Query
curl -X POST http://localhost:8000/ai/query \
  -H "Content-Type: application/json" \
  -d '{"query": "¿Qué es la diabetes?", "max_length": 200}'

# GitHub Stats
curl http://localhost:8000/github/stats
```

### Using Python Requests

```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# AI Query
data = {
    "query": "¿Qué es la diabetes?",
    "max_length": 200
}
response = requests.post("http://localhost:8000/ai/query", json=data)
print(response.json())
```

### Using JavaScript Fetch

```javascript
// Health check
fetch('http://localhost:8000/health')
  .then(response => response.json())
  .then(data => console.log(data));

// AI Query
fetch('http://localhost:8000/ai/query', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    query: '¿Qué es la diabetes?',
    max_length: 200
  })
})
  .then(response => response.json())
  .then(data => console.log(data));
```

## Interactive Documentation

For interactive API documentation, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
