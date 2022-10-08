import { observer } from "mobx-react-lite";
import type { NextPage } from "next";
import Head from "next/head";
import Image from "next/image";
import Container1 from "../components/landingContainers/Container 1/Container1";
import Container2 from "../components/landingContainers/Container 2/Container2";
import Container3 from "../components/landingContainers/Container 3/Container3";
import Container4 from "../components/landingContainers/Container 4/Container4";
import LandingLoginModal from "../components/landingLoginModal/LandingLoginModal";
import LandingTopBar from "../components/landingTopBar/LandingTopBar";
import styles from "../styles/landing.module.scss";

const Index: NextPage = () => {
  return (
    <>
      <Head>
        <title>ВТБ | Платформа</title>
        <link rel="icon" href="/favico/favicon.ico" />
      </Head>
      <div className={styles.indexContainer}>
        <LandingTopBar />
        <div className={styles.landingContainer}>
          <Container1 />
          <Container2 />
          <Container3 />
          <Container4 />
        </div>
      </div>
      <LandingLoginModal/>
    </>
  );
};

export default observer(Index);
