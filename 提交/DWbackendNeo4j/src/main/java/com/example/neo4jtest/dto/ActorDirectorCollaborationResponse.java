package com.example.neo4jtest.dto;

import java.util.List;

public class ActorDirectorCollaborationResponse {
    private List<ActorDirectorCollaboration> collaborations;
    private double time;

    public ActorDirectorCollaborationResponse(List<ActorDirectorCollaboration> collaborations, double time) {
        this.collaborations = collaborations;
        this.time = time;
    }

    // Getters and setters
    public List<ActorDirectorCollaboration> getCollaborations() {
        return collaborations;
    }

    public void setCollaborations(List<ActorDirectorCollaboration> collaborations) {
        this.collaborations = collaborations;
    }

    public double getTime() {
        return time;
    }

    public void setTime(double time) {
        this.time = time;
    }
}
