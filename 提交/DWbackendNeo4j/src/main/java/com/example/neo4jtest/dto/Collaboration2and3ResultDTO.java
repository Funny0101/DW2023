package com.example.neo4jtest.dto;

public class Collaboration2and3ResultDTO {
    private ActorDoubleCollaboration doubleCollaboration;
    private ActorTripleCollaboration tripleCollaboration;
    private double time; // 时间单位为秒

    // Constructor, Getters, and Setters
    public Collaboration2and3ResultDTO(ActorDoubleCollaboration doubleCollaboration, ActorTripleCollaboration tripleCollaboration, double executionTime) {
        this.doubleCollaboration = doubleCollaboration;
        this.tripleCollaboration = tripleCollaboration;
        this.time = executionTime;
    }

    public ActorDoubleCollaboration getDoubleCollaboration() {
        return doubleCollaboration;
    }

    public void setDoubleCollaboration(ActorDoubleCollaboration doubleCollaboration) {
        this.doubleCollaboration = doubleCollaboration;
    }

    public ActorTripleCollaboration getTripleCollaboration() {
        return tripleCollaboration;
    }

    public void setTripleCollaboration(ActorTripleCollaboration tripleCollaboration) {
        this.tripleCollaboration = tripleCollaboration;
    }

    public double getTime() {
        return time;
    }

    public void setTime(double time) {
        this.time = time;
    }

    public Collaboration2and3ResultDTO() {
    }
}
