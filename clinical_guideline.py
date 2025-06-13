def get_recommendation(subtype):
    recommendations = {
        'Luminal A': 'Terapi hormon biasanya efektif. Pertimbangkan Tamoxifen atau AI.',
        'Luminal B': 'Kombinasi terapi hormon dan kemoterapi direkomendasikan.',
        'HER2-positive': 'Pertimbangkan terapi target seperti Trastuzumab (Herceptin).',
        'Triple-negative': 'Kemoterapi adalah pilihan utama. Evaluasi respon secara berkala.',
    }
    return recommendations.get(subtype, "Tidak ada rekomendasi khusus.")

