import axios from "axios";
export const sendMessage = async (message) => {
  const res = await axios.post(
    process.env.REACT_APP_BACKEND_URL + "/chat",
    { message }
  );
  return res.data.response;
};
