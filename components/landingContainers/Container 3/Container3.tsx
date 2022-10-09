import styles from "./styles.module.scss";
import Image from "next/image";
import image from "../../../public/LPP/LPP3.png";
import imageNUM from "../../../public/LPP/LP3NUM.png";
import imageNUM2 from "../../../public/LPP/LP3NUM2.png";
import imageNUM3 from "../../../public/LPP/LP3NUM3.png";
import imageNUM4 from "../../../public/LPP/LP3NUM4.png";
import imageNUM5 from "../../../public/LPP/LP3NUM5.png";
import { useEffect, useState } from "react";
import { motion } from "framer-motion";

const Container3 = () => {
  const [scroll, setScroll] = useState(0);
  const [animation, setAnim] = useState({
    transform: "translateX(-25%)",
    opacity: 0,
  });
  const handleScroll = () => {
    setScroll(window.scrollY);

    if (window.scrollY >= 1500) {

      setAnim({ transform: "translateX(0%)", opacity: 1 });
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);
  return (
    <motion.div
      className={styles.containerThree}
      initial={{ transform: "translateX(-25%)", opacity: 0 }}
      animate={animation}
      transition={{ duration: 1, type: "spring" }}
    >
      <h1>Цели проекта</h1>
      <div className={styles.containerWN}>
        <p>Разработать веб-сервис, направленный на решение следующих задач</p>
        <Image src={imageNUM} />
      </div>
      <div className={styles.containerWN}>
        <Image src={imageNUM2} />
        <p>Работа с мотивацией и вовлеченностью сотрудников</p>
      </div>
      <div className={styles.containerWN}>
        <p>Создание профессиональных комьюнити</p>
        <Image src={imageNUM3} />
      </div>
      <div className={styles.containerWN}>
        <Image src={imageNUM4} />
        <p>Формирование культурного фундамента внутри компании</p>
      </div>
      <div className={styles.containerWN}>
        <p>Развитие HR-Brand как ИТ-компании</p>
        <Image src={imageNUM5} width={142} />
      </div>
    </motion.div>
  );
};

export default Container3;
