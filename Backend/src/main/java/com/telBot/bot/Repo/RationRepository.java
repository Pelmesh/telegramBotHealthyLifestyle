package com.telBot.bot.Repo;

import com.telBot.bot.model.Ration;
import com.telBot.bot.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RationRepository extends JpaRepository<Ration,Long> {

    List<Ration> findAllByUser(User user);
}
