import React, { useRef, useEffect, useState } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

const WebcamCapture = () => {
  const webcamRef = useRef(null);
  const [status, setStatus] = useState("Detecting...");

  const captureAndSend = async () => {
    if (!webcamRef.current) return;
    const screenshot = webcamRef.current.getScreenshot();
    if (!screenshot) return;

    const res = await fetch(screenshot);
    const blob = await res.blob();
    const formData = new FormData();
    formData.append("file", blob, "frame.jpg");

    try {
      const response = await axios.post("http://localhost:8000/detect", formData);
      setStatus(response.data.attention);
    } catch (error) {
      setStatus("Error");
    }
  };

  useEffect(() => {
    const interval = setInterval(captureAndSend, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="text-center">
      <Webcam
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        videoConstraints={{ facingMode: "user" }}
        style={{ width: "100%", maxWidth: 640 }}
      />
      <h2 className="mt-4 text-xl font-bold text-indigo-600">Status: {status}</h2>
    </div>
  );
};

export default WebcamCapture;
