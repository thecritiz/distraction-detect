import Hero from './components/Hero';
import LiveDemo from './components/LiveDemo';
import Features from './components/Features';
import CTA from './components/CTA';
import Footer from './components/Footer';

const App = () => (
  <div className="bg-gray-50 min-h-screen font-sans">
    <Hero />
    <LiveDemo />
    <Features />
    <CTA />
    <Footer />
  </div>
);

export default App;
