package com.example.neo4jtest.dto;

import java.util.List;

public class ActorCollaborationResponse {
    private List<ActorCollaboration> collaborations;
    private double time;

    public ActorCollaborationResponse(List<ActorCollaboration> collaborations, double time) {
        this.collaborations = collaborations;
        this.time = time;
    }

    // Getters and setters
    public List<ActorCollaboration> getCollaborations() {
        return collaborations;
    }

    public void setCollaborations(List<ActorCollaboration> collaborations) {
        this.collaborations = collaborations;
    }

    public double getTime() {
        return time;
    }

    public void setTime(double time) {
        this.time = time;
    }
}
