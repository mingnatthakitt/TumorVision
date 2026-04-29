import { motion } from 'framer-motion';

interface Props {
  name: string;
  description: string;
  images: string[];
  index: number;
}

export default function TumorCard({ name, description, images, index }: Props) {
  return (
    <motion.div
      className="tumor-card"
      initial={{ opacity: 0, y: 30 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-50px' }}
      transition={{ delay: index * 0.05, duration: 0.5 }}
    >
      <div className="tumor-card-images">
        {images.map((src, i) => (
          <img key={i} src={src} alt={`${name} MRI ${i + 1}`} loading="lazy" />
        ))}
      </div>
      <div className="tumor-card-body">
        <h3 className="tumor-card-title">{name}</h3>
        <p className="tumor-card-description">{description}</p>
      </div>
    </motion.div>
  );
}
