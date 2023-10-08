import Link from "next/link";
import styles from "./Home.module.css"
const Home = () => {
  return (
    <div className="w-screen h-screen bg-transparent text-center">
      <div className={styles.background}></div>
      <div className="top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 fixed z-0 ">
        <div className={styles.header} id={styles.header}>
          <h1 className={styles.header}>
            <span className={styles["rotate-one"]}>P</span>
            <span className={styles["rotate-two"]}>E</span>
            <span className={styles["rotate-one"]}>A</span>
            <span className={styles["rotate-two"]}>R</span>
          </h1>
        </div>
        <div className={styles["button-container"]}>
          <Link href={"/app"} className={styles.btn}>start</Link>
        </div>
      </div>
    </div>
  );
};
export default Home;
