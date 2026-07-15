import { useEffect, useState } from "react";
import { fetchDashboardStats } from "../services/dashboardService";

export default function useDashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadDashboard();
  }, []);

  async function loadDashboard() {
    try {
      const data = await fetchDashboardStats();
      setStats(data);
    } catch (err) {
      console.log(err);
    } finally {
      setLoading(false);
    }
  }

  return {
    stats,
    loading,
  };
}