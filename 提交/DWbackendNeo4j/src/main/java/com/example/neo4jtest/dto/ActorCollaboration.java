package com.example.neo4jtest.dto;

import java.io.Serializable;

public class ActorCollaboration implements Serializable {
    private static final long serialVersionUID = 1L; // 可选，但推荐

    private String actorName1;
    private String actorName2;
    private int collaborationCount;

    // 公开的无参构造函数
    public ActorCollaboration() {
    }

    // 带参数的构造函数
    public ActorCollaboration(String actorName1, String actorName2, int collaborationCount) {
        this.actorName1 = actorName1;
        this.actorName2 = actorName2;
        this.collaborationCount = collaborationCount;
    }

    // 公开的getter方法
    public String getActorName1() {
        return actorName1;
    }

    public String getActorName2() {
        return actorName2;
    }

    public int getCollaborationCount() {
        return collaborationCount;
    }

    // 公开的setter方法
    public void setActorName1(String actorName1) {
        this.actorName1 = actorName1;
    }

    public void setActorName2(String actorName2) {
        this.actorName2 = actorName2;
    }

    public void setCollaborationCount(int collaborationCount) {
        this.collaborationCount = collaborationCount;
    }
}
