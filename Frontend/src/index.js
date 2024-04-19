import React from 'react';
import ReactDOM from 'react-dom/client';
import { Auth0Provider } from "@auth0/auth0-react";
import App from './App';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Auth0Provider
    domain="dev-kwu3sywuy21eyhy5.us.auth0.com"
    clientId="vEiTHYJOD1idAmoIDlj1UOB4uZIvDljI"
    authorizationParams={{
      redirect_uri: window.location.origin
    }}
  >
  
    <App />
    </Auth0Provider>
  );

