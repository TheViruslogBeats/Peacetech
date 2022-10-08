import styles from "./styles.module.scss";
import Image from "next/image";
import profileImage1 from "../../../public/profilePhotos/1.jpg";
import profileImage2 from "../../../public/profilePhotos/2.jpg";
import profileImage3 from "../../../public/profilePhotos/3.jpeg";
import profileImage4 from "../../../public/profilePhotos/4.jpg";
import profileImage5 from "../../../public/profilePhotos/5.jpg";
import { useEffect, useState } from "react";
import { motion } from "framer-motion";

const Container4 = () => {
  let photoProps = {
    width: "142px",
    height: "142px",
  };
  const [scroll, setScroll] = useState(0);
  const [animation, setAnim] = useState({
    transform: "translateX(20%)",
    opacity: 0,
  });
  const handleScroll = () => {
    setScroll(window.scrollY);
    if (window.scrollY >= 2500) {

      setAnim({ transform: "translateX(0%)", opacity: 1 });
    }
  };

  useEffect(() => {
    window.addEventListener("scroll", handleScroll);
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);
  return (
    <motion.div
      className={styles.containerFour}
      initial={{ transform: "translateX(20%)", opacity: 0 }}
      animate={animation}
      transition={{ duration: 1, type: "spring" }}
    >
      <h1>Наша команда</h1>
      <div className={styles.comandContainer}>
        <div className={styles.personContainer}>
          <Image src={profileImage1} {...photoProps} />
          <h4>Хаметзянов Александр</h4>
          <p>UI/UX - Developer</p>
        </div>
        <div className={styles.personContainer}>
          <Image src={profileImage2} {...photoProps} />
          <h4>
            Разуваев <br /> Павел
          </h4>
          <p>Team-Leader</p>
        </div>
        <div className={styles.personContainer}>
          <Image src={profileImage3} {...photoProps} />
          <h4>
            Шматов <br /> Егор
          </h4>
          <p>Frontend Developer</p>
        </div>
        <div className={styles.personContainer}>
          <Image src={profileImage4} {...photoProps} />
          <h4>
            Скакодуб <br /> Геннадий
          </h4>
          <p>Backend Developer</p>
        </div>
        <div className={styles.personContainer}>
          <Image src={profileImage5} {...photoProps} />
          <h4>
            Соломатина <br /> Дарья
          </h4>
          <p>Business Analyst</p>
        </div>
      </div>
    </motion.div>
  );
};

export default Container4;
