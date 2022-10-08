import Image from "next/image";
import React from "react";
import PanelLayout from "../layouts/PanelLayout";
import styles from "./panel.module.scss";
import DR1 from "../public/DR 1.png";
import crown from "../public/crown.png";
import star from "../public/yellow star.png";
import { AiOutlineShoppingCart } from "react-icons/ai";
import { IoMdSchool } from "react-icons/io";
import { GiFireFlower } from "react-icons/gi";

const panel = () => {
  return (
    <PanelLayout>
      <div className={styles.container}>
        <div className={styles.miniContainer}>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(104.79deg, #0091A7 18.5%, rgba(0, 74, 191, 0) 100%);",
            }}
          >
            <p>Для благодарностей</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={DR1} />
              <h3>54.047</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(104.79deg, #003A95 -34.9%, rgba(0, 74, 191, 0) 100%); ",
            }}
          >
            <p>Мой статус</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={crown} />
              <h3>Цифровой гуру</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(104.24deg, #700083 -22.78%, rgba(112, 1, 129, 0.859375) -5.7%, rgba(113, 7, 122, 0) 98.68%);",
            }}
          >
            <p>Мои накопления</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={DR1} />
              <h3>54.047</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(107.23deg, #00954D -43.44%, rgba(0, 255, 133, 0) 100%); ",
            }}
          >
            <p>Мой рейтинг</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={star} />
              <h3>2075</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(107.23deg, #BA9100 -43.44%, rgba(186, 145, 0, 0) 100%);",
            }}
          >
            <p>Мои проекты</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={star} />
              <h3>13</h3>
            </div>
          </div>
        </div>
        <div
          className={styles.mainContainer}
          style={{
            background: "linear-gradient(180deg, #0091A7 0%, #113A7C   100%) ",
          }}
        ></div>
        <div className={styles.secondMC}>
          <div
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.38deg, rgba(117, 255, 222, 0.67) -8.05%, #113A7C 78.03%);",
            }}
          >
            <p>МАГАЗИН</p>
            <AiOutlineShoppingCart />
          </div>
          <div
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.38deg, #591263 -8.05%, #20117C 78.03%);",
            }}
          >
            <p>ОБУЧЕНИЕ</p>
            <IoMdSchool />
          </div>
          <div
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.5deg, #00C02A -8.06%, #20117C 77.13%);",
            }}
          >
            <p>МОЙ САД</p>
            <GiFireFlower />
          </div>
        </div>
      </div>
      <div>
        <div
          className={styles.infoBlock}
          style={{
            background:
              "linear-gradient(182.77deg, #002A6C -55.97%, rgba(0, 93, 240, 0) 113.16%);",
          }}
        ></div>
        <div
          className={styles.infoBlock}
          style={{
            background:
              "linear-gradient(182.77deg, #FFFFFF -55.97%, hsla(51, 100%, 27%, .25) 113.16%);",
          }}
        ></div>
      </div>
    </PanelLayout>
  );
};

export default panel;
