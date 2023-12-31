package com.example.neo4jtest.entity;

import org.springframework.data.neo4j.core.schema.Id;
import org.springframework.data.neo4j.core.schema.Node;

@Node
public class Actor {
    @Id
    private Integer actorId;
    private String actorName;

    // 构造函数
    public Actor() {}

    public Actor(Integer actorId, String actorName) {
        this.actorId = actorId;
        this.actorName = actorName;
    }

    // Getter和Setter
    public Integer getActorId() {
        return actorId;
    }

    public void setActorId(Integer actorId) {
        this.actorId = actorId;
    }

    public String getActorName() {
        return actorName;
    }

    public void setActorName(String actorName) {
        this.actorName = actorName;
    }
}
