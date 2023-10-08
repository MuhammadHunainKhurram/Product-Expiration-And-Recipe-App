import Head from "next/head";
import styles from "./index.module.css";
import Home from "~/components/Home";

const Page = () => {
  return (
    <div className="h-screen w-screen bg-transparent">
      <Head>
        <title>Pear</title>
      </Head>
      <Home />
    </div>
  );
};
export default Page;
