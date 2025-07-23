const features = [
  {
    title: "Real-time Detection",
    desc: "Get instant updates on attention using facial landmarks and head pose estimation.",
  },
  {
    title: "Lightweight",
    desc: "FastAPI + MediaPipe powered backend optimized for low-latency requests.",
  },
  {
    title: "Easy Integration",
    desc: "Access via REST API. Plug it into your LMS or system in minutes.",
  },
];

const Features = () => (
  <section className="py-16 bg-gray-100">
    <div className="max-w-5xl mx-auto grid grid-cols-1 md:grid-cols-3 gap-8 text-center">
      {features.map(({ title, desc }) => (
        <div key={title} className="bg-white p-6 shadow rounded-2xl">
          <h3 className="text-xl font-semibold mb-2">{title}</h3>
          <p className="text-gray-600">{desc}</p>
        </div>
      ))}
    </div>
  </section>
);

export default Features;
