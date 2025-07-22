import React from 'react';
import WebcamCapture from './components/WebcamCapture';

function App() {
  return (
    <div className="p-4 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6 text-center">Attentiveness Checker</h1>
      <WebcamCapture />
    </div>
  );
}

export default App;
