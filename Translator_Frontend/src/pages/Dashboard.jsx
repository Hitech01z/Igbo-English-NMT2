import useDashboard from "../hooks/useDashboard";

import StatCard from "../components/dashboard/StatCard";

import {
    Database,
    Languages,
    FileText,
    BookOpen
} from "lucide-react";

export default function Dashboard() {

    const { stats, loading } = useDashboard();

if (loading) {
    return (
        <div className="flex justify-center py-20">
            Loading Dashboard...
        </div>
    );
}

if (!stats) {
    return (
        <div className="flex justify-center py-20 text-red-500">
            Failed to load dashboard.
        </div>
    );
}

    return (

        <div className="space-y-8">

            <h1 className="text-3xl font-bold">
                Dashboard
            </h1>

            <div className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">

                <StatCard
                    title="Dataset Size"
                    value={stats.dataset_size}
                    color="bg-blue-500 text-white"
                    icon={<Database />}
                />

                <StatCard
                    title="Vocabulary Size"
                    value={stats.vocabulary_size}
                    color="bg-purple-500 text-white"
                    icon={<Languages />}
                />

                <StatCard
                    title="Domains"
                    value={stats.domains}
                    color="bg-green-500 text-white"
                    icon={<BookOpen />}
                />

                <StatCard
                    title="Translations"
                    value={stats.total_translations}
                    color="bg-orange-500 text-white"
                    icon={<FileText />}
                />
     

            </div>

        </div>

    );

}