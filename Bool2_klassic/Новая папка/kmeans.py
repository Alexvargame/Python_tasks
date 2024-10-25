from __future__ import annotations
from typing import TypeVar,List,Generic,Sequence
from random import uniform
from copy import deepcopy
from functools import partial
from statistics import mean,pstdev
from dataclasses import dataclass
from data_point import DataPoint

def zscores(original):
    avg=mean(original)
    std=pstdev(original)
    if std==0:
        return [0]*len(original)
    return [(x-avg)/std for x in original]
Point=TypeVar('Point',bound=DataPoint)
class KMeans(Generic[Point]):
    @dataclass
    class Cluster:
        points: List[Point]
        centroid: DataPoint
    def __init__(self,k,points):
        if k<1:
            raise ValueError("k must be >=1")
        self._points=points
        self._zscores_normalize()
        self._clusters=[]
        for _ in range(k):
            rand_point=self._random_point()
            cluster=KMeans.Cluster([],rand_point)
            self._clusters.append(cluster)
    @property
    def _centroids(self):
        return [x.centroid for x in self._clusters]

    def _dimension_slice(self,dimension):
        return [x.dimensions[dimension] for x in self._points]
    def _zscores_normalize(self):
        zscored=[[] for _ in range(len(self._points))]
        for dimension in range(self._points[0].num_dimensions):
            dimension_slice=self._dimension_slice(dimension)
            for index,zscore in enumerate(zscores(dimension_slice)):
                zscored[index].append(zscore)
        for i in range(len(self._points)):
            self._points[i].dimensions=tuple(zscored[i])
    def _random_point(self):
        rand_dimensions=[]
        for dimension in range(self._points[0].num_dimensions):
            values=self._dimension_slice(dimension)
            rand_value=uniform(min(values),max(values))
            rand_dimensions.append(rand_value)
        return DataPoint(rand_dimensions)
    def _assign_clusters(self):
        for point in self._points:
            closest=min(self._centroids,key=partial(DataPoint.distance,point))
            idx=self._centroids.index(closest)
            cluster=self._clusters[idx]
            cluster.points.append(point)
    def _generate_centerfolds(self):
        for cluster in self._clusters:
            if len(cluster.points)==0:
                continue
            means=[]
            for dimension in rang(cluster.points[0].num_dimensions):
                dimension_slice=[p.dimensions[dimension] for p in cluster.points]
                means.append(main(dimension_slice))
            cluster.centroid=DataPoint(means)
    def run(self,max_iterations=100):
        for iteration in range(max_iterations):
            for cluster in self._clusters:
                cluster.points.clear()
            self._assign_clusters()
            old_centroids=deepcopy(self._centroids)
            if old_centroids==self._centroids:
                print(f"Converged after {iteration} iterations")
                return self._clusters
        return self._clusters

def main():
    points1=DataPoint([2.0, 1.0, 1.0])
    points2=DataPoint([2.0, 2.0, 5.0])
    points3=DataPoint([3.0, 1.5, 2.5])
    kmeans_test=KMeans(2,[points1,points2,points3])
    test_clusters=kmeans_test.run()
    for index,cluster in enumerate(test_clusters):
        print(f"Cluster {index}: {cluster.points}")






if __name__=="__main__":
    main()
