import WebcamCapture from './WebcamCapture';

const LiveDemo = () => (
  <section className="py-16 bg-white">
    <div className="max-w-4xl mx-auto">
      <h2 className="text-3xl font-semibold text-center mb-6">Live Attention Status</h2>
      <WebcamCapture />
    </div>
  </section>
);

export default LiveDemo;
