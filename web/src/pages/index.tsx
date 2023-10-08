import * as Dialog from "@radix-ui/react-dialog";
import Head from "next/head";
import Link from "next/link";
import {
  type SetStateAction,
  useEffect,
  useRef,
  useState,
  type Dispatch,
} from "react";
import { Camera, type CameraType } from "react-camera-pro";

const sendImage = async (image: string) => {
  const nutrition = await fetch("http://localho.st:5000/barcode", {
    method: "PUT",
    mode: "cors",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({ image: image }),
  });
};

export default function Home() {
  const [cameraOpen, setCameraOpen] = useState(false);
  return (
    <>
      <Head>
        <title>CookMe</title>
        <meta name="description" content="hackuta 2023" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <div className="flex flex-row p-2">
          Header
          <FoodSearch />
          <div>
            <Dialog.Root open={cameraOpen} onOpenChange={setCameraOpen}>
              <Dialog.Trigger asChild={true}>
                <button
                  type="button"
                  className="rounded-lg bg-green-600 p-2 text-white hover:bg-green-700"
                >
                  add with camera
                </button>
              </Dialog.Trigger>
              <Dialog.Portal>
                <Dialog.Overlay className="fixed inset-0 h-screen w-screen bg-black opacity-30" />
                <Dialog.Content>
                  <div className="fixed left-1/2 top-1/2 h-fit w-fit -translate-x-1/2 -translate-y-1/2 rounded-md bg-white p-10">
                    <CameraWrap setCameraOpen={setCameraOpen} />
                  </div>
                </Dialog.Content>
              </Dialog.Portal>
            </Dialog.Root>
          </div>
        </div>
        <div className="p-2">
          <FoodItem
            food={{
              name: "Gerble - sesame cookie",
              ingredients: ["Farine de ble"],
              energy: 54,
            }}
          />
        </div>
      </main>
    </>
  );
}
type Food = {
  energy: number;
  ingredients: Array<string>;
  name: string;
  nova?: number;
  expiry?: number;
};

type FoodItemProps = {
  food: Food;
};

const FoodSearch = () => {
  return (
    <div>
      <input type="text" className="box-content" />
    </div>
  );
};

const FoodItem = ({ food }: FoodItemProps) => {
  const [expanded, setExpanded] = useState();
  return (
    <div className="flex flex-col rounded-lg bg-slate-200 p-2">
      <div>
        <h1 className="text-xl font-extrabold">{food.name}</h1>
        <h2 className="text-base">Expires soon</h2>
      </div>
      <div className="text-lg">Calories per serving: {food.energy}</div>
      <div>
        <h2 className="text-lg">Ingredients</h2>
      </div>
    </div>
  );
};
type CameraProps = {
  setCameraOpen: Dispatch<SetStateAction<boolean>>;
};
const CameraWrap = ({ setCameraOpen }: CameraProps) => {
  const camera = useRef<CameraType>(null);
  const [devices, setDevices] = useState<MediaDeviceInfo[]>([]);
  const [activeDevice, setActiveDevice] = useState<string | undefined>(
    undefined,
  );
  const [image, setImage] = useState<string | undefined>(undefined);
  useEffect(() => {
    void (async () => {
      const devices = await navigator.mediaDevices.enumerateDevices();
      const videoDevices = devices.filter((i) => i.kind === "videoinput");
      setDevices(videoDevices);
    })();
  });
  return (
    <div className="flex flex-col">
      <button className="box-content" onClick={() => setCameraOpen(false)}>
        close
      </button>
      <div className="container relative h-[30rem] w-[30rem]">
        <Camera
          ref={camera}
          aspectRatio={"cover"}
          videoSourceDeviceId={activeDevice}
          errorMessages={{
            noCameraAccessible:
              "No camera device accessible. Please connect your camera or try a different browser.",
            permissionDenied:
              "Permission denied. Please refresh and give camera permission.",
            switchCamera:
              "It is not possible to switch camera to different one because there is only one video device accessible.",
            canvas: "Canvas is not supported.",
          }}
        />
      </div>
      <div>
        <h3>Select camera</h3>
        <select
          onChange={(e) => {
            setActiveDevice(e.target.value);
          }}
        >
          {devices.map((device) => (
            <option key={device.deviceId} value={device.deviceId}>
              {device.label}
            </option>
          ))}
        </select>
      </div>
      <button
        type="button"
        className="box-content"
        onClick={() => {
          const photo = camera.current?.takePhoto();
          if (photo) {
            void sendImage(photo)
              .catch((reason) => {
                console.error(reason);
              })
              .then((value) => {
                console.log(value);
              });
          }
        }}
      >
        take photo
      </button>
      <div>
        <div
          className="h-[120px] w-[120px] bg-contain"
          style={{ backgroundImage: `url(${image})` }}
        ></div>
      </div>
    </div>
  );
};
