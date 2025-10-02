# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 19:32:16 2025

@author: ferryas

Secara keseluruhan, visualisasi menunjukkan bagaimana nilai awal dari 'Supply' 
(Pendidikan, Penelitian, Pengabdian) mengalir melalui sistem, menghasilkan 'Output', 
memenuhi 'Demand', dan memicu 'Kolaborasi' serta 'Rekognisi'. 
Terdapat feedback loop di mana kolaborasi dan kapasitas kembali memperkuat pilar supply,
 menciptakan siklus yang dinamis.
"""

import networkx as nx
import matplotlib.pyplot as plt
#from collections import deque
#import numpy as np

class TridharmaDataFlow:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.node_values = {}
        self.initialize_graph()
    
    def initialize_graph(self):
        """Inisialisasi node dan edge berdasarkan diagram"""
        # Define nodes dengan atribut
        nodes = {
            "P1": {"type": "supply", "name": "Pendidikan & Pembelajaran", "value": 10},
            "P2": {"type": "supply", "name": "Penelitian & Inovasi Terapan", "value": 8},
            "P3": {"type": "supply", "name": "Pengabdian & Hilirisasi", "value": 7},
            "CGrad": {"type": "output", "name": "Kompetensi Lulusan", "value": 0},
            "Proto": {"type": "output", "name": "Prototipe/Tech Siap Uji", "value": 0},
            "Policy": {"type": "output", "name": "Kebijakan/Standar & Dampak Sosial", "value": 0},
            "DUDI": {"type": "demand", "name": "Industri/DUDI", "value": 5},
            "ACAD": {"type": "demand", "name": "Komunitas Akademik", "value": 4},
            "PUB": {"type": "demand", "name": "Pemerintah & Publik", "value": 3},
            "COL": {"type": "collaboration", "name": "Kinerja Kolaborasi", "value": 0},
            "REC": {"type": "recognition", "name": "Rekognisi Portofolio", "value": 0},
            "CAREER": {"type": "support", "name": "Karier/Jafung & Pendanaan", "value": 0},
            "CAP": {"type": "capacity", "name": "Capacity: Waktu & Sumber Daya", "value": 6},
            "ADMIN": {"type": "constraint", "name": "Beban Administratif", "value": 4},
            "ALIGN": {"type": "incentive", "name": "Keselarasan Insentif", "value": 0}
        }
        
        # Add nodes ke graph
        for node_id, attributes in nodes.items():
            self.graph.add_node(node_id, **attributes)
            self.node_values[node_id] = attributes["value"]
        
        # Define edges dengan bobot pengaruh
        edges = [
            # Supply -> Output
            ("P1", "CGrad", {"weight": 0.5, "label": "supply-output(1)"}),
            ("P2", "Proto", {"weight": 0.8, "label": "supply-output(2)"}),
            ("P3", "Policy", {"weight": 0.8, "label": "supply-output(3)"}),
            
            # Output -> Demand
            ("CGrad", "DUDI", {"weight": 0.8, "label": "output-demand(1)"}),
            ("Proto", "DUDI", {"weight": 0.6, "label": "output-demand(2)"}),
            ("Proto", "ACAD", {"weight": 0.7, "label": "output-demand(3)"}),
            ("Policy", "PUB", {"weight": 0.8, "label": "output-demand(4)"}),
            
            # Demand -> Collaboration
            ("DUDI", "COL", {"weight": 0.60, "label": "demand-kolaborasi(1)"}),
            ("PUB", "COL", {"weight": 0.20, "label": "demand-kolaborasi(2)"}),
            ("ACAD", "COL", {"weight": 0.20, "label": "demand-kolaborasi(3)"}),
            
            # Collaboration feedback loop
            ("COL", "P1", {"weight": 0.5, "label": "kolaborasi-supply(loop-1)"}),
            ("COL", "P2", {"weight": 0.6, "label": "kolaborasi-supply(loop-2)"}),
            ("COL", "P3", {"weight": 0.8, "label": "kolaborasi-supply(loop-3)"}),
            
            # Recognition system
            ("COL", "REC", {"weight": 0.5, "label": "rekognisi-daya dukung(1)"}),
            ("CGrad", "REC", {"weight": 0.6, "label": "rekognisi-daya dukung(2)"}),
            ("Proto", "REC", {"weight": 0.7, "label": "rekognisi-daya dukung(3)"}),
            ("Policy", "REC", {"weight": 0.8, "label": "rekognisi-daya dukung(4)"}),
            
            # Career and capacity
            ("REC", "CAREER", {"weight": 0.5, "label": "rekognisi-daya dukung(1)"}),
            ("CAREER", "CAP", {"weight": 0.5, "label": "rekognisi-daya dukung(2)"}),
            
            # Capacity reinforcement
            ("CAP", "P1", {"weight": 0.6, "label": "reinforcing semua pilar(1)"}),
            ("CAP", "P2", {"weight": 0.5, "label": "reinforcing semua pilar(2)"}),
            ("CAP", "P3", {"weight": 0.6, "label": "reinforcing semua pilar(3)"}),
            
            # Administrative burden (negative effect)
            ("ADMIN", "CAP", {"weight": -0.5, "label": "Decreases"}),
            ("REC", "ADMIN", {"weight": -0.5, "label": "Reduces"}),
            
            # Incentive alignment
            ("REC", "ALIGN", {"weight": 0.8, "label": "aturan menyelaraskan insentif"}),
            ("ALIGN", "COL", {"weight": 0.2, "label": "insentif selaras mendorong kolaborasi"})
        ]
        
        for from_node, to_node, attributes in edges:
            self.graph.add_edge(from_node, to_node, **attributes)
    
    
    
    def simulate_data_flow(self, iterations=10):
        """Simulasi aliran data melalui graph"""
        print("=== SIMULASI DATA FLOW TRIDHARMA ===")
        
        for iteration in range(iterations):
            print(f"\n--- Iterasi {iteration + 1} ---")
            
            # Buat salinan nilai node untuk update simultan
            new_values = self.node_values.copy()
            
            # Proses setiap node
            for node in self.graph.nodes():
                current_value = self.node_values[node]
                total_input = 0
                
                # Hitung input dari incoming edges
                for predecessor in self.graph.predecessors(node):
                    edge_data = self.graph[predecessor][node]
                    input_value = self.node_values[predecessor] * edge_data['weight']
                    total_input += input_value
                
                # Update nilai node (dengan decay factor untuk stabilitas)
                if total_input != 0:
                    new_values[node] = max(0, current_value * 0.7 + total_input * 0.3)
                
                print(f"{node}: {current_value:.2f} → {new_values[node]:.2f}")
            
            self.node_values = new_values
            
            # Tampilkan metrics penting
            self.calculate_metrics(iteration + 1)
    
   
    def calculate_metrics(self, iteration):
        """Hitung metrics performa sistem"""
        total_supply = sum(self.node_values[node] for node in ["P1", "P2", "P3"])
        total_demand = sum(self.node_values[node] for node in ["DUDI", "ACAD", "PUB"])
        collaboration_score = self.node_values["COL"]
        recognition_score = self.node_values["REC"]
        
        print(f"\n📊 METRICS Iterasi {iteration}:")
        print(f"   Total Supply: {total_supply:.2f}")
        print(f"   Total Demand: {total_demand:.2f}")
        print(f"   Score Kolaborasi: {collaboration_score:.2f}")
        print(f"   Score Rekognisi: {recognition_score:.2f}")
        
        # Cek equilibrium
        supply_demand_ratio = total_supply / total_demand if total_demand > 0 else 0
        if 0.9 <= supply_demand_ratio <= 1.1:
            print("   ✅ Supply-Demand Seimbang")
        elif supply_demand_ratio < 0.9:
            print("   ⚠️  Supply Kurang (Under-supply)")
        else:
            print("   ⚠️  Supply Berlebih (Over-supply)")
    
    def visualize_graph(self):
        """Visualisasi graph dengan nilai terkini"""
        plt.figure(figsize=(16, 12))
        
        # Layout yang lebih terorganisir
        pos = {
            # Supply nodes di kiri
            "P1": (0, 2), "P2": (0, 1), "P3": (0, 0),
            # Output nodes di tengah kiri
            "CGrad": (2, 2), "Proto": (2, 1), "Policy": (2, 0),
            # Demand nodes di tengah kanan
            "DUDI": (4, 2), "ACAD": (4, 1), "PUB": (4, 0),
            # Collaboration dan Recognition di tengah
            "COL": (3, 1.5), "REC": (3, 0.5),
            # Support system di kanan
            "CAREER": (5, 1.5), "CAP": (5, 0.5),
            # Constraints di bawah
            "ADMIN": (2, -1), "ALIGN": (4, -1)
        }
        
        # Warna berdasarkan tipe node
        node_colors = []
        for node in self.graph.nodes():
            node_type = self.graph.nodes[node]['type']
            if node_type == 'supply': node_colors.append('#FFCDD2')
            elif node_type == 'output': node_colors.append('#C5CAE9')
            elif node_type == 'demand': node_colors.append('#C8E6C9')
            elif node_type == 'collaboration': node_colors.append('#FFE0B2')
            elif node_type == 'recognition': node_colors.append('#FFCCBC')
            elif node_type == 'support': node_colors.append('#B3E5FC')
            elif node_type == 'capacity': node_colors.append('#E1BEE7')
            elif node_type == 'constraint': node_colors.append('#F8BBD0')
            else: node_colors.append('#FFFFFF')
        
        # Gambar nodes dengan size berdasarkan nilai
        node_sizes = [200 + self.node_values[node] * 50 for node in self.graph.nodes()]
        
        nx.draw_networkx_nodes(self.graph, pos, 
                              node_color=node_colors,
                              node_size=node_sizes,
                              alpha=0.9)
        
        # Gambar edges dengan warna berdasarkan weight
        edge_colors = []
        for u, v in self.graph.edges():
            weight = self.graph[u][v]['weight']
            if weight > 0:
                edge_colors.append('green')
            else:
                edge_colors.append('red')
        
        nx.draw_networkx_edges(self.graph, pos,
                              edge_color=edge_colors,
                              arrows=True,
                              arrowsize=20,
                              arrowstyle='->')
        
        # Label nodes dengan nama dan nilai
        labels = {}
        for node in self.graph.nodes():
            labels[node] = f"{node}\n({self.node_values[node]:.1f})"
        
        nx.draw_networkx_labels(self.graph, pos, labels, font_size=8)
        
        # Edge labels
        edge_labels = nx.get_edge_attributes(self.graph, 'label')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels, font_size=6)
        
        plt.title("Simulasi Data Flow Tridharma Perguruan Tinggi\n(Supply-Demand System)")
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def analyze_system_health(self):
        """Analisis kesehatan sistem"""
        print("\n=== ANALISIS KESEHATAN SISTEM ===")
        
        # Hitung berbagai metrics
        collaboration_effectiveness = self.node_values["COL"] / max(self.node_values["REC"], 1)
        supply_efficiency = sum(self.node_values[node] for node in ["CGrad", "Proto", "Policy"]) / sum(self.node_values[node] for node in ["P1", "P2", "P3"])
        administrative_efficiency = 1 - (self.node_values["ADMIN"] / max(self.node_values["CAP"], 1))
        
        print(f"Efektivitas Kolaborasi: {collaboration_effectiveness:.2f}")
        print(f"Efisiensi Supply: {supply_efficiency:.2f}")
        print(f"Efisiensi Administratif: {administrative_efficiency:.2f}")
        
        # Rekomendasi
        if collaboration_effectiveness < 0.5:
            print("🔧 REKOMENDASI: Tingkatkan mekanisme kolaborasi industri-akademik")
        if supply_efficiency < 0.6:
            print("🔧 REKOMENDASI: Optimasi proses tridharma untuk output lebih baik")
        if administrative_efficiency < 0.7:
            print("🔧 REKOMENDASI: Kurangi beban administratif dengan digitalisasi")
            
            
    # Tambahkan intervensi kebijakan
    def apply_policy_intervention(self, policy_type, intensity):
        """Terapkan intervensi kebijakan"""
        if policy_type == "reduce_admin":
            self.node_values["ADMIN"] *= (1 - intensity)
        elif policy_type == "boost_collaboration":
        # Tingkatkan bobot edge kolaborasi
            for edge in self.graph.edges():
                if "kolaborasi" in self.graph[edge[0]][edge[1]]['label']:
                    self.graph[edge[0]][edge[1]]['weight'] += intensity * 0.1



# Jalankan Simulasi
if __name__ == "__main__":
    # Inisialisasi sistem
    system = TridharmaDataFlow()
    system.apply_policy_intervention("reduce_admin", 0.3)  # Kurangi admin 30%
    # Jalankan simulasi
    system.simulate_data_flow(iterations=8)
    
    # Visualisasi hasil
    system.visualize_graph()
    
    # Analisis kesehatan sistem
    system.analyze_system_health()