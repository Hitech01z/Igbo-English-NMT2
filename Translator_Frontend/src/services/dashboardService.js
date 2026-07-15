import api from "./api";

export const fetchDashboardStats = async () => {
  return await api.get("/dashboard/");
};