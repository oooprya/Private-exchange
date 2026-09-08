// components/DamagedGallery.tsx
import Image from "next/image";
import styles from "./index.module.css";

const images = [
  "/damaged/1.jpg",
  "/damaged/2.jpg",
  "/damaged/3.jpg",
  "/damaged/4.jpg",
  "/damaged/5.jpg",
  "/damaged/6.jpg",
  "/damaged/7.jpg",
  "/damaged/8.jpg",
];

export default function DamagedGallery() {
  return (
    <section className="bg-black py-14">
      <div className="container mx-auto px-4">
        {/* TITLE */}
        <h2 className={styles.h2}>
          Навіть <span className={styles.textYellow}>такі купюри</span> ми візьмемо у вас
        </h2>

        {/* GRID */}
        <div className={styles.grid}>
          {images.map((src, index) => (
            <div
              key={index}
              className="relative overflow-hidden rounded-xl border border-zinc-800 bg-zinc-900"
            >
              <Image
                src={src}
                alt="Пошкоджені купюри долара та євро"
                width={270}
                height={360}
                className="h-full w-full object-cover transition-transform duration-300 hover:scale-105"
              />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
