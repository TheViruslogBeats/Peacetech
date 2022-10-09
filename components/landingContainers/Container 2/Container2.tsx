import styles from "./styles.module.scss";
import Image from "next/image";
import image from "../../../public/LPP/LPP2.png";
import { useState, useEffect } from "react";
import { motion } from "framer-motion";

const Container2 = () => {
  const [scroll, setScroll] = useState(0);
  const [animation, setAnim] = useState({
    transform: "translateX(20%)",
    opacity: 0,
  });
  const handleScroll = () => {
    setScroll(window.scrollY);

    if (window.scrollY >= 700) {
      setAnim({ transform: "translateX(0%)", opacity: 1 });
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
          ВТБ Платформа — корпоративная платформа с элементами геймификации для
          работы в сфере банкинга, а так же развития HR сферы, как IT бренда.
          Данная платформа реализована согласно концепции ВТБ в сфере ESG -
          environment, social, governance. Платформа дает возможность повысить
          мотивацию сотрудников во влечение в корпоративные сервисы банка, а так
          же улучшить свои личностные и профессиональные навыки.
        </p>
      </div>
    </motion.div>
  );
};

export default Container2;
