import styles from "./styles.module.scss";
import Image from "next/image";
import image from "../../../public/LPP/LPP2.png";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";

const Container2 = () => {
  const [scroll, setScroll] = useState(0);
  const [animation, setAnim] = useState({ transform: "translateX(20%)", opacity: 0 })
  const handleScroll = () => {
    setScroll(window.scrollY);
    
    if(window.scrollY >= 700) {
      
      setAnim({ transform: "translateX(0%)", opacity: 1 })
    }
  };


  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);
  return (
    <motion.div
      className={styles.containerTwo}
      initial={{ transform: "translateX(20%)", opacity: 0 }}
      animate={animation}
      transition={{ duration: 1, type: "spring" }}
    >
      <Image src={image} />
      <div>
        <h1>О проекте </h1>
        <p>
          Хакатон (от слов hacking — поиск нестандартных решений и marathon) —
          это командное соревнование для программистов, дизайнеров, менеджеров и
          аналитиков, которые в сжатые сроки решают социальную или
          бизнес-задачу: разрабатывают прототип, содержащий основной функционал.
        </p>
      </div>
    </motion.div>
  );
};

export default Container2;
