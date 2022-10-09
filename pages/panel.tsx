import Image from "next/image";
import React, { useEffect, useState } from "react";
import PanelLayout from "../layouts/PanelLayout";
import styles from "./panel.module.scss";
import DR1 from "../public/DR 1.png";
import crown from "../public/crown.png";
import star from "../public/yellow star.png";
import WT from "../public/WT.png";
import { AiOutlineShoppingCart } from "react-icons/ai";
import { IoMdSchool } from "react-icons/io";
import { GiFireFlower } from "react-icons/gi";
import api from "../states/api";
import { observer } from "mobx-react-lite";
import MainImage from "../public/Man Online.png";
import { TbArrowsDoubleNeSw } from "react-icons/tb";
import { IoHomeOutline } from "react-icons/io5";

const panel = () => {
  useEffect(() => {
    api.getLogin();
    api.getRole();
    api.getPR();
    api.getStatus();
    api.getCOT();
    api.getWB();
    api.getNWB();
    api.getTasks();
    // api.getPRID();
  }, []);

  const [modalMagazine, setModalMagazine] = useState(false);
  const [garden, setGarden] = useState(false);
  return (
    <PanelLayout>
      <div className={styles.container}>
        <div className={styles.miniContainer}>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(104.79deg, #0091A7 18.5%, rgba(0, 74, 191, 0) 100%)",
            }}
          >
            <p>Water Token</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={WT} />
              <h3>{api.userData.tokens[0].tokens.length}</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(104.79deg, #003A95 -34.9%, rgba(0, 74, 191, 0) 100%)",
            }}
          >
            <p>Мой статус</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={crown} />
              <h3>{api.userData.status}</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(104.24deg, #700083 -22.78%, rgba(112, 1, 129, 0.859375) -5.7%, rgba(113, 7, 122, 0) 98.68%)",
            }}
          >
            <p>Мои накопления</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={DR1} />
              <h3>{api.userData.digRub}</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(107.23deg, #00954D -43.44%, rgba(0, 255, 133, 0) 100%)",
            }}
          >
            <p>Мой рейтинг</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={star} />
              <h3>{api.userData.rating.score}</h3>
            </div>
          </div>
          <div
            className={styles.Card}
            style={{
              background:
                "linear-gradient(107.23deg, #BA9100 -43.44%, rgba(186, 145, 0, 0) 100%)",
            }}
          >
            <p>Мои задачи</p>
            <div className={styles.hr}></div>
            <div className={styles.CardInfo}>
              <Image src={star} />
              <h3>{api.userData.count}</h3>
            </div>
          </div>
        </div>
        <div
          className={styles.mainContainer}
          style={{
            background: "linear-gradient(180deg, #0091A7 0%, #113A7C   100%)",
          }}
        >
          <h2>
            Механизмы начисления и списания NFT-сертификатов и монет «Digital
            Ruble»
          </h2>
          <div>
            <Image src={MainImage} />
            <div>
              <p>
                Выбирай росток в теплице, покупай его за Water token`ы и сажай в
                своем саду. Каждое растение соответствует определенной задаче.
                Чем больше ты прикладываешь усилий к задаче, тем лучше и
                красивее твое дерево. После выполнения задачи получай награду в
                Digital Rubles, достижения и NFT растения в твою коллекцию,
                пусть все заходят и смотрят какой ты активный и полезный
                сотрудник. Water token`ы будут начисляться тебе администратором
                платформы каждый месяц.
              </p>
              <p>
                За каждое достижение ты получишь очки рейтинга и специальные
                бейджи, которые выделят тебя на фоне остальных в лидерборде и
                может быть к тебе заглянет один из топ-менеджеров и
                дополнительно поощрит тебя за хорошую работу.
              </p>
              <p>
                Зарабатывай больше Digital rubles чтобы накопить на ценные призы
                из магазина или отправлять в качестве благодарности коллегам.
              </p>
              <p>
                Разобраться тебе поможет наш маскот Рума - он амурский тигр,
                очень редкий и красивый. Не игнорируй его и не забывай выполнять
                задания, иначе он уйдет в какой-нибудь другой банк.{" "}
              </p>
            </div>
          </div>
        </div>
        <div className={styles.secondMC}>
          <div
            onClick={() => {
              setModalMagazine(true);
            }}
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.38deg, rgba(117, 255, 222, 0.67) -8.05%, #113A7C 78.03%)",
            }}
          >
            <p>МАГАЗИН</p>
            <AiOutlineShoppingCart />
          </div>
          <div
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.38deg, #591263 -8.05%, #20117C 78.03%)",
            }}
          >
            <p>ОБУЧЕНИЕ</p>
            <IoMdSchool />
          </div>
          <div
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.5deg, #00C02A -8.06%, #20117C 77.13%)",
            }}
            onClick={() => {
              setGarden(true);
            }}
          >
            <p>МОЙ САД</p>
            <GiFireFlower />
          </div>
          <div
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.5deg, #A500C0 -8.06%, #20117C 77.13%)",
            }}
          >
            <p>МОИ ОПЕРАЦИИ</p>
            <TbArrowsDoubleNeSw />
          </div>
          <div
            className={styles.SecondCard}
            style={{
              background:
                "linear-gradient(99.5deg, #00C02A -8.06%, #20117C 77.13%)",
            }}
          >
            <p>ТЕПЛИЦА</p>
            <IoHomeOutline />
          </div>
        </div>
      </div>
      <div>
        <div
          className={styles.infoBlock}
          style={{
            background:
              "linear-gradient(182.77deg, #002A6C -55.97%, rgba(0, 93, 240, 0) 113.16%)",
          }}
        >
          <h3>Мои задания 1/4</h3>
          <div className={styles.hr}></div>
          <div className={styles.infoList}>
            {api.userData.tasks.map((task) => {
              return (
                <div className={styles.Task}>
                  <h4>{task.description}</h4>
                  <p>Награда: {task.award} DigRub</p>
                </div>
              );
            })}
          </div>
        </div>
        <div
          className={styles.infoBlock}
          style={{
            background:
              "linear-gradient(182.77deg, #FFFFFF -55.97%, hsla(51, 100%, 27%, .25) 113.16%)",
          }}
        >
          <h3>Лидеры платформы</h3>
          <div className={styles.hr}></div>
          <div className={styles.infoList}>
            <div className={styles.userInfoList}>
              <p>№1</p>
              <img
                src="https://cdn.discordapp.com/attachments/934798571688054914/1024374884819808357/691235880.jpeg"
                alt=""
              />
              <div>
                <p>Шматов Егор Сергеевич</p>
                <p>
                  Очки: 12415 <Image src={WT} width={19} height={24} />
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div
        className={styles.modalMagazine}
        style={{ display: modalMagazine ? "flex" : "none" }}
        onClick={() => {
          setModalMagazine(false);
        }}
      >
        <h2>МАГАЗИН</h2>
        <h2>Еда Мероприятия Конвертация Одежда Для дома</h2>
        <div className={styles.hr}></div>
        <ul>
          <li>
            <div>
              <p>Кроссовки</p>
              <img
                src="https://cdn.discordapp.com/attachments/934798571688054914/1028462012042334269/unknown.png"
                alt=""
              />
              <button>В корзину</button>
            </div>
            <div>
              <p>
                <b>Описание</b>
              </p>
              <p>
                Кроссовки Nike Внутри модели установлены мягкие вставки. В
                области пятки
              </p>
            </div>
          </li>
          <li>
            <div>
              <p>Кроссовки</p>
              <img
                src="https://cdn.discordapp.com/attachments/934798571688054914/1028462012042334269/unknown.png"
                alt=""
              />
              <button>В корзину</button>
            </div>
            <div>
              <p>
                <b>Описание</b>
              </p>
              <p>
                Кроссовки Nike Внутри модели установлены мягкие вставки. В
                области пятки
              </p>
            </div>
          </li>
          <li>
            <div>
              <p>Кроссовки</p>
              <img
                src="https://cdn.discordapp.com/attachments/934798571688054914/1028462012042334269/unknown.png"
                alt=""
              />
              <button>В корзину</button>
            </div>
            <div>
              <p>
                <b>Описание</b>
              </p>
              <p>
                Кроссовки Nike Внутри модели установлены мягкие вставки. В
                области пятки
              </p>
            </div>
          </li>
          <li>
            <div>
              <p>Кроссовки</p>
              <img
                src="https://cdn.discordapp.com/attachments/934798571688054914/1028462012042334269/unknown.png"
                alt=""
              />
              <button>В корзину</button>
            </div>
            <div>
              <p>
                <b>Описание</b>
              </p>
              <p>
                Кроссовки Nike Внутри модели установлены мягкие вставки. В
                области пятки
              </p>
            </div>
          </li>
        </ul>
      </div>
      <div
        className={styles.modalGarden}
        style={{ display: garden ? "flex" : "none" }}
        onClick={() => {
          setGarden(false);
        }}
      >
        <img
          src="https://cdn.discordapp.com/attachments/934798571688054914/1028477490806673468/1.png"
          alt=""
        />
      </div>
    </PanelLayout>
  );
};

export default observer(panel);
