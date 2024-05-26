from KnowledgeFrames import Frame
from KnowledgeFrames import knowledgeFrames

def main():
    # базовый фрейм "Комнаты"
    base_room_frame = Frame('Комната')
    base_room_frame.set_slot('Тип', 'Жилое помещение')
    base_room_frame.set_slot('Кол-во стен', 4)
    base_room_frame.set_slot('Тип пола', 'Деревянный')
    base_room_frame.set_slot('Цвет потолка', 'Белый')

    # Наследник комнаты - "Спальня"
    bedroom_frame = Frame("Спальня", parent_frame=base_room_frame)
    bedroom_frame.set_slot('Кол-во окон', 2)
    bedroom_frame.set_slot('Площадь, м^2', 20)

    # Наследник комнаты "Гостинная"
    living_room_frame = Frame('Гостинная', parent_frame=base_room_frame)
    living_room_frame.set_slot('Кол-во окон', 3)
    living_room_frame.set_slot('Площадь, м^2', 35)
    living_room_frame.set_slot('Тип пола', 'Мраморная плитка')

    knowledge_frames = knowledgeFrames()
    knowledge_frames.add_entry(base_room_frame.frame_name, base_room_frame)
    knowledge_frames.add_entry(bedroom_frame.frame_name, bedroom_frame)
    knowledge_frames.add_entry(living_room_frame.frame_name, living_room_frame)
    
    print(knowledge_frames)

if __name__ == '__main__':
    main()