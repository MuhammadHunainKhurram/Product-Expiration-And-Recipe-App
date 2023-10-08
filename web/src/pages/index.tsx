import * as Dialog from "@radix-ui/react-dialog";
import Head from "next/head";
import Link from "next/link";
import { type SetStateAction, useEffect, useRef, useState, type Dispatch } from "react";
import { Camera, type CameraType } from "react-camera-pro";



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
                <button type="button" className="p-2 bg-green-600 text-white rounded-lg hover:bg-green-700">
                  add with camera</button>
              </ Dialog.Trigger>
              <Dialog.Portal>
                <Dialog.Overlay className="fixed bg-black opacity-30 w-screen h-screen inset-0" />
                <Dialog.Content>
                  <div className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 bg-white p-10 rounded-md w-fit h-fit">
                    <CameraWrap setCameraOpen={setCameraOpen} />
                  </div>
                </Dialog.Content>
              </ Dialog.Portal>
            </Dialog.Root>
          </div>
        </div>
        <div className="p-2">
          <FoodItem food={{ name: "Gerble - sesame cookie", ingredients: ["Farine de ble"], energy: 54 }} />
        </div>
      </main>
    </>
  );
}
type Food = {
  energy: number,
  ingredients: Array<string>,
  name: string,
  nova?: number,
  expiry?: number
}

type FoodItemProps = {
  food: Food;
}

const FoodSearch = () => {
  return <div>
    <input type="text" className="box-content" />
  </div>
}

const FoodItem = ({ food }: FoodItemProps) => {
  const [expanded, setExpanded] = useState();
  return (<div className="flex flex-col p-2 bg-slate-200 rounded-lg">
    <div>
      <h1 className="font-extrabold text-xl">{food.name}</h1>
      <h2 className="text-base">Expires soon</h2>
    </div>
    <div className="text-lg">
      Calories per serving: {food.energy}
    </div>
    <div>
      <h2 className="text-lg">Ingredients</h2>
    </div>
  </div>)


}
type CameraProps = {
  setCameraOpen: Dispatch<SetStateAction<boolean>>
}
const CameraWrap = ({ setCameraOpen }: CameraProps) => {
  const camera = useRef<CameraType>(null);
  const [devices, setDevices] = useState<MediaDeviceInfo[]>([])
  const [activeDevice, setActiveDevice] = useState<string | undefined>(undefined)
  const [image, setImage] = useState<string | undefined>(undefined);
  useEffect(() => {
    void (async () => {
      const devices = await navigator.mediaDevices.enumerateDevices();
      const videoDevices = devices.filter((i) => i.kind === "videoinput");
      setDevices(videoDevices);
    })();
  });
  return <div className="flex flex-col">
    <button className="box-content" onClick={() => setCameraOpen(false)}>close</button>
    <div className="container h-[30rem] w-[30rem] relative">
      <Camera ref={camera} aspectRatio={"cover"} videoSourceDeviceId={activeDevice} errorMessages={{
        noCameraAccessible: 'No camera device accessible. Please connect your camera or try a different browser.',
        permissionDenied: 'Permission denied. Please refresh and give camera permission.',
        switchCamera:
          'It is not possible to switch camera to different one because there is only one video device accessible.',
        canvas: 'Canvas is not supported.',
      }} />
    </div>
    <div>
      <h3>Select camera</h3>
      <select onChange={(e) => { setActiveDevice(e.target.value) }}>
        {devices.map((device) => <option key={device.deviceId} value={device.deviceId}>
          {device.label}
        </option>)}
      </select>
    </div>
    <button type="button" className="box-content" onClick={() => {
      const photo = camera.current?.takePhoto();
      setImage(photo);
    }}>take photo</button>
    <div>
      <div className="h-[120px] w-[120px] bg-contain" style={{ backgroundImage: `url(${image})` }}></div>
    </div>
  </div>
}
