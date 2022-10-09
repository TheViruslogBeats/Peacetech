import Image from "next/image";
import styles from "./styles.module.scss";
import image from "../../../public/LPP/LPP1.png";
import landingPage from "../../../states/landingPage";
import { motion } from "framer-motion";

const Container1 = () => {
  
  return (
    <motion.div
      className={styles.containerOne}
      initial={{ transform: "translateX(-25%)", opacity: 0 }}
      animate={{ transform: "translateX(0%)", opacity: 1 }}
      transition={{duration: 1, type: "spring"}}
    >
      <div>
        <div>
          <h1>Внутренний портал сотрудника</h1>
          <p>
          Зарабатывай больше Digital rubles чтобы накопить на ценные призы из магазина или отправлять в качестве благодарности коллегам.

          </p>
          <button
            onClick={() => {
              landingPage.setLM(true);
            }}
          >
            Войти
          </button>
        </div>
        <Image src={image} className={styles.img} />
      </div>
    </motion.div>
  );
};

export default Container1;
