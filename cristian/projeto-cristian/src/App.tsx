import { useState } from 'react'
import './App.css'
import fotoMinha from "./assets/fotominha.png"
import { SocialIcon } from 'react-social-icons'
import { TypeAnimation } from 'react-type-animation';
import Wave from 'react-wavify'



function App() {

   const QuemEh = () => {
  return (
    <TypeAnimation
      sequence={[
        // Same substring at the start will only be typed out once, initially
        '🤔⁉️',
        1000, // wait 1s before replacing "Mice" with "Hamsters"
        'Quem é Cristian?',
      ]}
      wrapper="span"
      speed={50}
      style={{ fontSize: '2em', display: 'inline-block' }}
      repeat={Infinity}
    />
   
  );

};

  return (
    <>

<div className="min-h-screen bg-red-300 p-8 rounded-lg relative">

              <div className="relative z-10 p-8 rounded-lg">
        <h1 className="text-4xl font-bold mb-8 flex items-center gap-3 text-center justify-center">
        {QuemEh()}
        </h1>
        <div className="flex flex-col md:flex-row gap-8 mb-8">
          <section className="bg-gray-50 rounded-lg shadow p-8 flex items-center justify-center md:w-1/3">
            <img src={fotoMinha} className="rounded-full w-40 h-40 object-cover" />
          </section>
          <section className="bg-gray-50 rounded-lg shadow p-8 flex-1">
            <h2 className="text-2xl font-extrabold mb-4 text-gray-800">Sobre mim:</h2>
            <p className="text-gray-800 font-bold">
              Olá! Meu nome é Cristian, sou desenvolvedor apaixonado por tecnologia e inovação. Tenho experiência com React, TypeScript e Tailwind CSS. Gosto de arte e coisas bonitas, por isso estou buscando seguir carreira no front-end.
              Meus hobbies são:
              <p className="text-gray-600 font-normal">
                ✏️ Desenhar, 🎮 Jogar videogame, 📺 Assistir animes, 📖 Ler livros.
              </p>
            </p>      
          </section>

          
        </div>

      <div className="flex flex-col md:flex-row gap-8 mb-8">
        <section className="bg-gray-50 rounded-lg shadow p-8">
          <h2 className="text-2xl font-extrabold mb-4 text-gray-800">🎓 Formação:</h2>
          <ul className="list-disc pl-5 text-gray-800 space-y-2">
            <li>Graduado em Publicidade e Propaganda, pela Universidade Estácio de Sá, desde 2023.</li>
            <li>Cursando Licenciatura em Computação, pela UFERSA, desde 2021.</li>
            <li>Cursando pós-graduação em Robótica Educacional, desde 2025.</li>
          </ul>
        </section>

        <section className="bg-gray-50 rounded-lg shadow p-8">
          <h2 className="text-2xl font-extrabold mb-4 text-gray-800">💼 Experiência profissional:</h2>
          <ul className="list-disc pl-5 text-gray-800 space-y-2">
            <li>
              Professor de Robótica na Robo Ciência - Atual;
            </li>
            <li>
              Auxiliar de comunicação no Núcleo de Arte e Cultura, UFERSA - 2023 à 2024;
            </li>
            <li>
              Social Media, Colégio Sagrado Coração de Maria - 2022 à 2024;
            </li>
            <li>
              Diagramador, Colégio Pequeno Príncipe - 2018 à 2022;
            </li>
          </ul>
        </section>

            <section className="bg-gray-50 rounded-lg shadow p-8 flex flex-col">
              <h2 className="text-2xl font-extrabold mb-4 text-gray-800 text-center">📞 Contatos:</h2>
              <div className="flex flex-col gap-4 w-full">
              <p className="text-gray-800 flex items-center gap-2 justify-start">
                <SocialIcon url="https://instagram.com/cristianmenoli" style={{ height: 25, width: 25 }}/>
                @cristianmenoli
              </p>
              <p className="text-gray-800 flex items-center gap-2 justify-start">
                <SocialIcon url="mailto:oemcristian@gmail.com" style={{ height: 25, width: 25 }}/>
                oemcristian@gmail.com
              </p>
              <p className="text-gray-800 flex items-center gap-2 justify-start">
                <SocialIcon url="wa.me/+5584999140782" style={{ height: 25, width: 25 }}/>
                +5584999140782
              </p>
              </div>
            </section>

        </div>
        </div>
        <Wave fill='#f79902'
          paused={false}
          style={{ display: 'flex' }}
          options={{
            height: 20,
            amplitude: 20,
            speed: 0.50,
            points: 3
          }}
                    className="absolute inset-0 z-0 h-150 mt-105"
        />
      </div>
       
    </>
  )
}

export default App
