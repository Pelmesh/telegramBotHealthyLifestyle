package com.telBot.bot.api;

import com.telBot.bot.Repo.UserRepository;
import com.telBot.bot.model.Body;
import com.telBot.bot.model.Role;
import com.telBot.bot.model.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

import java.util.Collections;
import java.util.List;
import java.util.Random;

@EnableSwagger2
@RestController
@RequestMapping("/api/user")
public class UserApiController {

    @Autowired
    private UserRepository userRepository;

    @GetMapping
    public List<User> getAllUsers(){
        return  userRepository.findAll();
    }

    @GetMapping("{idChat}")
    public User getByIdChat(@PathVariable Long idChat){
        return  userRepository.findByIdChat(idChat);
    }

    @PostMapping
    public User saveUser(@RequestBody User user){
        user.setPassword(getPas());
        user.setRoles(Collections.singleton(Role.USER));
        user.setUsername(user.getIdChat().toString());
        return userRepository.save(user);
    }


    public String getPas(){
        char[] chars = "abcdef12345689QWERTYUISAD".toCharArray();
        StringBuilder sb = new StringBuilder(8);
        Random random = new Random();
        for (int i = 0; i < 8; i++) {
            char c = chars[random.nextInt(chars.length)];
            sb.append(c);
        }
        return sb.toString();
    }

}
