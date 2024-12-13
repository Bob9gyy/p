# Proxy Server with Password Protection

This project implements a simple proxy server with password protection using FastAPI, designed for deployment on Vercel.

## Features
- **Password Protection**: Clients must provide a valid password in the `Authorization` header.
- **Request Forwarding**: Forwards HTTP requests to a target URL specified in the `X-Target-URL` header.
- **Deployable on Vercel**: Designed to work seamlessly with Vercel's serverless infrastructure.

## Setup

### Local Development
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
